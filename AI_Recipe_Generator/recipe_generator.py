import os
import cv2

# === CONFIGURATION ===
images = [
    {
        "img_path": r"C:\Users\WIN 11\OneDrive\Desktop\AI_Recipe_Generator\yolov5\runs\detect\exp\Fp1.jpg",
        "txt_path": r"C:\Users\WIN 11\OneDrive\Desktop\AI_Recipe_Generator\yolov5\runs\detect\exp\labels\Fp1.txt"
    },
    {
        "img_path": r"C:\Users\WIN 11\OneDrive\Desktop\AI_Recipe_Generator\yolov5\runs\detect\exp2\Fp2.jpg",
        "txt_path": r"C:\Users\WIN 11\OneDrive\Desktop\AI_Recipe_Generator\yolov5\runs\detect\exp2\labels\Fp2.txt"
    },
    {
        "img_path": r"C:\Users\WIN 11\OneDrive\Desktop\AI_Recipe_Generator\yolov5\runs\detect\exp5\Fp3.jpg",
        "txt_path": r"C:\Users\WIN 11\OneDrive\Desktop\AI_Recipe_Generator\yolov5\runs\detect\exp5\labels\Fp3.txt"
    }
]

# === YOLOv5 COCO class index to ingredient names mapping ===
coco_labels = {
    46: "banana", 47: "apple", 49: "orange", 50: "broccoli", 51: "carrot", 52: "carrot",
    53: "hotdog", 55: "sandwich", 58: "pizza"
}

# === Recipes Database ===
recipes = {
    "apple": ["Apple pie", "Apple salad"],
    "banana": ["Banana smoothie", "Banana pancakes"],
    "carrot": ["Carrot halwa", "Carrot soup"],
    "orange": ["Orange juice", "Orange zest cake"],
    "sandwich": ["Veg sandwich", "Grilled cheese"],
    "broccoli": ["Broccoli stir-fry", "Broccoli soup"],
    "pizza": ["Veg pizza", "Cheese pizza"],
    "hotdog": ["Classic hotdog", "Veg hotdog"]
}

# === Final Output Storage ===
output_file = "recipes_output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write("🍽️ AI Recipe Suggestions\n\n")

# === PROCESSING ===
for index, item in enumerate(images):
    image_path = item["img_path"]
    label_path = item["txt_path"]
    detected_items = []

    if os.path.exists(label_path):
        with open(label_path, "r") as file:
            for line in file:
                class_index = int(line.strip().split()[0])
                label = coco_labels.get(class_index)
                if label:
                    detected_items.append(label)

    detected_items = list(set(detected_items))  # remove duplicates

    # Get Recipes
    suggested_recipes = set()
    for ing in detected_items:
        suggested_recipes.update(recipes.get(ing, []))

    # === Show Image ===
    img = cv2.imread(image_path)

    # Resize to max width/height while keeping aspect ratio
    max_width = 1800
    max_height = 700
    height, width = img.shape[:2]
    scaling_factor = min(max_width / width, max_height / height)
    resized_img = cv2.resize(img, (int(width * scaling_factor), int(height * scaling_factor)))

    # Show the image
    cv2.imshow(f"Image {index+1}", resized_img)
    cv2.waitKey(4000)  # Show for 4000 milliseconds = 4 seconds
    cv2.destroyAllWindows()


    # === Print and Save Output ===
    print(f"\nImage {index+1}: {os.path.basename(image_path)}")
    print("Detected:", detected_items if detected_items else "None")
    print("Recipes:", list(suggested_recipes) if suggested_recipes else "No recipes found")

    with open(output_file, "a", encoding="utf-8") as f:
        f.write(f"\nImage {index+1}: {os.path.basename(image_path)}\n")
        f.write(f"Detected: {', '.join(detected_items) if detected_items else 'None'}\n")
        f.write("Recipes: " + (", ".join(suggested_recipes) if suggested_recipes else "No recipes found") + "\n")

print(f"\n✅ All suggestions saved to '{output_file}'")
