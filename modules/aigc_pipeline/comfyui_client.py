import requests
import json
import time
import random
import os
from PIL import Image
from io import BytesIO

class ComfyUIClient:
    def __init__(self, server_url="http://127.0.0.1:8188"):
        self.server_url = server_url
        self.workflow_path = os.path.join(
            os.path.dirname(__file__), 
            "workflow.json"
        )
    
    def load_workflow(self):
        with open(self.workflow_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def queue_prompt(self, prompt):
        response = requests.post(f"{self.server_url}/prompt", json={"prompt": prompt})
        return response.json()
    
    def get_history(self, prompt_id):
        response = requests.get(f"{self.server_url}/history/{prompt_id}")
        return response.json()
    
    def generate_image(self, positive_prompt, seed=None, width=512, height=512):
        try:
            workflow = self.load_workflow()
            print("Workflow loaded successfully")
        except Exception as e:
            print(f"Failed to load workflow: {e}")
            return self._simulate_image()
        
        # Set positive prompt (node 16)
        if "16" in workflow and workflow["16"]["class_type"] == "CLIPTextEncodeFlux":
            workflow["16"]["inputs"]["clip_l"] = positive_prompt
            workflow["16"]["inputs"]["t5xxl"] = positive_prompt
            print(f"Positive prompt set: {positive_prompt[:80]}...")
        else:
            print("Warning: Node 16 not found or wrong type")
        
        # Set random seed (node 18)
        if "18" in workflow and workflow["18"]["class_type"] == "KSampler (Efficient)":
            if seed is not None:
                workflow["18"]["inputs"]["seed"] = seed
            else:
                workflow["18"]["inputs"]["seed"] = random.randint(1, 2**31)
            print(f"Seed set: {workflow['18']['inputs']['seed']}")
        else:
            print("Warning: Node 18 not found")
        
        # Set image size (node 19)
        if "19" in workflow and workflow["19"]["class_type"] == "EmptyLatentImage":
            workflow["19"]["inputs"]["width"] = width
            workflow["19"]["inputs"]["height"] = height
            print(f"Size set: {width}x{height}")
        else:
            print("Warning: Node 19 not found")
        
        # Submit task
        try:
            print("Submitting task...")
            result = self.queue_prompt(workflow)
            print(f"Submit result: {result}")
            prompt_id = result.get("prompt_id")
            if not prompt_id:
                print("No prompt_id received")
                return self._simulate_image()
            
            # Poll for result
            timeout = 60
            start_time = time.time()
            while time.time() - start_time < timeout:
                history = self.get_history(prompt_id)
                if prompt_id in history:
                    outputs = history[prompt_id]["outputs"]
                    # Get image from SaveImage node (ID 21)
                    if "21" in outputs and "images" in outputs["21"]:
                        image_data = outputs["21"]["images"][0]
                        filename = image_data["filename"]
                        image_url = f"{self.server_url}/view?filename={filename}&type=output"
                        print(f"Fetching image: {image_url}")
                        img_response = requests.get(image_url)
                        img = Image.open(BytesIO(img_response.content))
                        return img  # Return PIL Image directly
                time.sleep(1)
            print("Timeout waiting for image")
            return self._simulate_image()
        except Exception as e:
            print(f"Error during image generation: {e}")
            return self._simulate_image()
    
    def _simulate_image(self):
        """Fallback simulated image"""
        img = Image.new('RGB', (512, 512), color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        return img
    
    def generate_with_cultural_style(self, ip_element, style="traditional"):
        # English prompt templates for cultural IPs
        prompt_map = {
            "Dunhuang Flying Apsaras": {
                "traditional": "Dunhuang Flying Apsaras, Tang Dynasty style, flowing ribbons, auspicious clouds, playing pipa backwards, mural texture, mineral pigment colors, elegant and antique, exquisite lines, prosperous Tang atmosphere",
                "modern": "Dunhuang Flying Apsaras, cyberpunk style, neon lights, futuristic technology, digital art, high saturation colors, mechanical wings, holographic projection, city background",
                "fusion": "Dunhuang Flying Apsaras merged with surrealism, fluid forms, light and shadow interplay, deconstruction of cultural symbols, transparent materials, dreamy atmosphere, colorful, abstract expression"
            },
            "Suzhou Embroidery": {
                "traditional": "Suzhou embroidery, Jiangnan water town, flowers, birds, fish, insects, silk luster, delicate stitching, gongbi style, soft colors, elegant and exquisite, intangible cultural heritage",
                "modern": "Suzhou embroidery elements combined with modern design, geometric patterns, bright colors, abstract textures, digital printing, fashion sense, installation art",
                "fusion": "Suzhou embroidery merged with light and shadow art, flowing silk, combination of virtual and real, three-dimensional embroidery, interactive projection, cultural innovation, visual impact"
            },
            "Kunqu Opera": {
                "traditional": "Kunqu opera, Peony Pavilion, Du Liniang, water sleeves dance, opera makeup, gorgeous costumes, stage setting, classical garden, poetic and beautiful",
                "modern": "Kunqu opera and modern stage art, light and shadow interplay, abstract space, dramatic tension, avant-garde design, multimedia integration, youthful expression",
                "fusion": "Kunqu opera merged with digital art, particle effects, motion capture, reconstruction of cultural symbols, immersive experience, surreal atmosphere"
            },
        }
        
        # Default English templates for other IPs
        default_templates = {
            "traditional": f"Traditional Chinese art style, {ip_element}, ink wash painting, gongbi painting, exquisite details, antique elegance, profound artistic conception",
            "modern": f"Modern digital art, {ip_element}, cyberpunk, neon lights, high saturation, futuristic, technological sense, Chinese trendy elements",
            "fusion": f"East-West fusion, {ip_element}, abstract expressionism, deconstruction of cultural symbols, surreal, strong colors, light and shadow interplay"
        }
        
        # Check if ip_element matches any key (case-insensitive approximate)
        matched_key = None
        for key in prompt_map.keys():
            if key.lower() in ip_element.lower() or ip_element.lower() in key.lower():
                matched_key = key
                break
        
        if matched_key and style in prompt_map[matched_key]:
            positive_prompt = prompt_map[matched_key][style]
        else:
            positive_prompt = default_templates.get(style, default_templates["traditional"])
        
        return self.generate_image(positive_prompt)