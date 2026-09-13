print("Welcome to FitBot!")
bot_name: str = "COACH"
print(f"Hello I \'M {bot_name}! How can I help you today?")

while True:
    user_input: str = input("You: ").lower()
    if user_input in["hello","hi"]:
        print(f"{bot_name}: How can I help you today?")
    elif user_input in["bye","exit"]:
        print(f"{bot_name}: Good bye ")
        break
    elif "protein" in user_input:
     print(f"{bot_name}: Eat 1.6g to 2.2g of protein per kg daily!")
    elif "workout" in user_input:
         print(f"{bot_name}: Push / Pull / Legs is a great split to build muscle!")
    elif "water" in user_input:
           weight_input = input(f"{bot_name}: Enter your weight in KG: ")
           if weight_input.isdigit():
            weight = float(weight_input)
            water_liters = (weight * 35) / 1000
            print(f"{bot_name}: Based on your weight ({weight}kg), you should drink around {water_liters:.2f} Liters of water daily!")

           else:
             print(f"{bot_name}: Please enter a valid number for weight next time!")
    else :
        print(f"{bot_name}: I didn't understand that. Ask me about protein or workout!")   
