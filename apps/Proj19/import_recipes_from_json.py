import json

def import_recipes(db, file):
    with open(file) as f:
        meals = json.load(f)['meals']
        for meal in meals:
            name = meal['strMeal'] if meal['strMeal'] else 'None'
            type = meal['strArea'] if meal['strArea'] else 'None'
            category = meal['strCategory']
            tags = meal['strTags']
            youtube = meal['strYoutube']
            description = ""
            if category:
                description += category + ", "
            if tags:
                description += tags + ", "
            if youtube:
                description += youtube + ", "
            if len(description) > 0:
                description = description[:-2]
            author = "TheMealDB"
            instruction_steps = meal['strInstructions'] if meal['strInstructions'] else 'None'
            servings = 1
            db.recipe.insert(name=name, type=type, description=description, author=author, instruction_steps=instruction_steps, servings=servings)
            db.commit()

            for i in range(1, 21):
                ingredient = meal['strIngredient' + str(i)]
                measure = meal['strMeasure' + str(i)]
                # Do something linking recipe and ingredients
