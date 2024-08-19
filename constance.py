class IngredientsBurger:
    correct_burger = {
        "ingredients":  [
            "61c0c5a71d1f82001bdaaa70",
            "61c0c5a71d1f82001bdaaa72",
            "61c0c5a71d1f82001bdaaa6c"
            ]
        }

    incorrect_burger = {
        "ingredients":  [
            "60c0c5a71d1f82001bdaaa70",
            "60c0c5a71d1f82001bdaaa72",
            "60c0c5a71d1f82001bdaaa6c"
        ]
    }

    not_ingredients_burger = {
        "ingredients": [

        ]
    }


class StatusMessage:
    not_id_ingredients = "Ingredient ids must be provided"
    not_authorised = "You should be authorised"
    incorrect_data = "email or password are incorrect"
    duplicate_user = "User already exists"
    not_field_data = "Email, password and name are required fields"
