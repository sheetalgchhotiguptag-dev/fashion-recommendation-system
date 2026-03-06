# Fashion Recommendation System
# Simple AI-based outfit suggestion

def recommend_outfit(weather, occasion):

    if weather == "summer":
        if occasion == "casual":
            return "Cotton T-shirt with Jeans"
        elif occasion == "party":
            return "Light Summer Dress"
        elif occasion == "office":
            return "Formal Shirt with Trousers"

    elif weather == "winter":
        if occasion == "casual":
            return "Sweater with Jeans"
        elif occasion == "party":
            return "Stylish Coat with Dress"
        elif occasion == "office":
            return "Blazer with Formal Pants"

    elif weather == "rainy":
        if occasion == "casual":
            return "Waterproof Jacket with Jeans"
        elif occasion == "party":
            return "Short Dress with Boots"
        elif occasion == "office":
            return "Formal Wear with Raincoat"

    return "No recommendation available"


# User Input
print("AI Fashion Recommendation System")

weather = input("Enter weather (summer/winter/rainy): ")
occasion = input("Enter occasion (casual/party/office): ")

outfit = recommend_outfit(weather, occasion)

print("Recommended Outfit:", outfit)
