def parse_ingredient(ingredient_info):
    ingredient_info = ingredient_info.split(' | ')
    ingredient_name = ingredient_info[0]
    quantity = int(ingredient_info[1])
    measure = ingredient_info[2]
    return {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}


def skip_empty_line(file):
    file.readline()


def read_recipe(file):
    recipe_name = file.readline().strip()
    if not recipe_name:
        return None

    ingredient_count = int(file.readline().strip())
    ingredients = [parse_ingredient(file.readline().strip()) for _ in range(ingredient_count)]

    skip_empty_line(file)

    return recipe_name, ingredients


def read_recipes(file_name):
    cook_book = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        while True:
            recipe_data = read_recipe(file)
            if recipe_data is None:
                break

            recipe_name, ingredients = recipe_data
            cook_book[recipe_name] = ingredients

    return cook_book


file_name = 'recipes.txt'
cook_book = read_recipes(file_name)
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shop_list[ingredient_name]['quantity'] += quantity
    return shop_list

# тестим
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
print(shop_list)
