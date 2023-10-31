import os
from pathlib import Path
from os import system


# welcome user / directory path / number files (recipes)
recipes_path_str = os.getcwd()
main_folder = "Recetas"


def get_main_folder(path):
    """
    Take path (string), check if it's main_folder and return the path instance
    :param path: path variable (string) to convert into Path
    :return: current path as Path instance
    """
    current_path = Path(path)
    if main_folder not in path.split('/'):
        # Add to end path the main folder name
        current_path = Path(path, main_folder)
    else:
        # If in the last position of the path have main folder name
        current_path = [p for p in current_path.parents if str(p).split('/')[-1] == main_folder][0]
        # print('current path', current_path)
    return current_path


# clean console fn
def clean_console():
    # check OS
    o_s = os.name  # operative system name
    if o_s == 'posix':  # Linux & macOS
        system('clear')
    elif o_s == 'nt':   # Windows
        system('cls')


def welcome_recipes(user, global_path):
    """
    Give welcome user and print directory path and number recipes in
    """
    clean_console()
    print("#" * 50)
    print("#" * 16, "RECIPES PROGRAM", "#" * 16)
    print("#" * 50)
    # get directory path and recipes
    recipes_path = get_main_folder(global_path)
    recipe_list = [path.stem for path in Path(recipes_path).glob("**/*.txt")]
    # user name
    while user == '':
        user = input("Type your name |> ")
        user = ''.join(user.split(' '))
        # user_name = user_name + user
        print()
        print(f"Welcome {user},")
    print(f"""
    The recipes are in
    {recipes_path} path,
    with {len(recipe_list)} recipes to enjoy.
    """)
    return user, recipes_path


def recipe_options():
    """
    Return the option selected by the user
    :return: an integer
    """
    option = -1
    while int(option) not in range(0, 6):
        print("""Do you want to:
        [1] Read recipe
        [2] Create recipe
        [3] Delete recipe
        [4] Create a recipe category
        [5] Delete a recipe category
        [0] Finish program""")
        option = input(f"""|> """)
        if not option.isnumeric():
            option = -1
    return int(option)


# category recipe selecting
def recipe_category_selection(categories):
    """
    Return the recipe to read/create/delete a recipe or,
     a recipe category to delete
    :return: recipe string
    """
    categories.sort()
    print()
    print("Select a category")
    for idx, ctg in enumerate(categories):
        print(f"[{idx + 1}] {ctg}")
    nb_category = -1
    while nb_category == -1:
        nb_category = input("# category |> ")
        # check entry
        if (not nb_category.isnumeric() or
                (int(nb_category) - 1) not in range(0, len(categories))):
            nb_category = -1
            continue
        confirm = ''
        nb_category = int(nb_category) - 1
        while confirm.lower() not in ['y', 'n']:
            confirm = input(f"You choose {categories[nb_category]} category?"
                            f"(y/n)_ ")
        if confirm == 'n':
            nb_category = -1
    print()

    return categories[nb_category]


# getting paths
def getting_recipes_path(recipes_path, categories_list):
    """
    Get the path to recipe category and recipe files
    :param recipes_path:
    :param categories_list:
    :return: recipe file path
    """
    # select category/folder
    category_path = Path(
        recipes_path,
        recipe_category_selection(categories_list)
    )

    # listing recipes
    recipes_list = list(category_path.glob("*.txt"))
    if len(recipes_list) == 0:
        print("This category doesn't have recipes\n"
              "Please create a recipe")
        return ""
    print()
    print(f'Select a recipe:')
    for idx, file in enumerate(category_path.glob("*.txt")):
        recipes_list.append(file)
        print(f"[{idx + 1}] {file.stem}")
    recipe_nb = -1
    while recipe_nb not in range(0, len(list(category_path.glob("*.txt")))):
        recipe_nb = int(input("|> ")) - 1

    return recipes_list[recipe_nb]


# Read recipe flow
def read_recipe_fn(recipes_path, categories_list):
    """
    Read a file that user choose
    :param recipes_path:
    :param categories_list:
    """
    if len(categories_list) == 0:
        print("Recipe categories has not been created yet\n"
              "Please create a category\n")
        return
    # get paths
    recipe_file_path = getting_recipes_path(
        recipes_path, categories_list
    )
    if recipe_file_path == "":
        return
    # open file to read
    recipe_lines = open(str(recipe_file_path), 'r')
    print()
    # name file comes in th format "name_recipe.txt", so we replace the "_" with " ".
    print("======================================================================")
    print(f"""
    {' '.join(recipe_file_path.stem.split('_'))}
    --------------------\n
    {recipe_lines.read()}
    """)
    print("======================================================================")
    recipe_lines.close()


# Create recipe flow - function
def create_recipe_fn(recipes_path, category_list):
    """
    Create a recipe file in a recipe category
    :param recipes_path: recipes main folder
    :param category_list: category recipes list
    :return:
    """
    # select category/folder
    category = recipe_category_selection(category_list)

    # enter recipe info: recipe name and content
    new_recipe_path = Path("")
    recipe_name = ""
    file_exist = False
    while not file_exist:
        print("file_exist", file_exist, "not file_exist", not file_exist)
        recipe_name = input(" Type recipe name |> ")
        recipe_name = recipe_name.replace(' ', '_')
        new_recipe_path = Path(recipes_path, f'{category}/{recipe_name}.txt')
        # if file exist, return False
        if not os.path.exists(new_recipe_path):
            print(f"{new_recipe_path} \nfile exists")
            file_exist = True
        else:
            file_exist = False

    recipe_content_lines = []
    print("You can add many lines. Use '0' to stop enter content/lines")
    li = ''
    while li != '0':
        li = input("Type line |> ")
        if li != '0':
            recipe_content_lines.append(li)
    # create recipe/file (.txt)
    new_recipe = open(new_recipe_path, 'a')
    for li in recipe_content_lines:
        new_recipe.writelines(f"{li}\n")
    new_recipe.close()
    print(f"...'{recipe_name}' recipe was created successfully...")


# Delete recipe function
def delete_recipe_fn(recipes_path, categories_list):
    # get paths
    recipe_file_path = getting_recipes_path(
        recipes_path, categories_list
    )
    if recipe_file_path == "":
        return
    ask_delete = ''
    try:
        while ask_delete not in ['y', 'n']:
            ask_delete = input(f'Do you want to delete {recipe_file_path.stem} file? (y/n) ')
        if ask_delete == 'y':
            Path(recipe_file_path).unlink()
            print(f"{recipe_file_path.stem} file was deleted")
    except Exception as e:
        print(f"An error has occurred: \n{str(e)}")


# Create recipe category function
def create_recipe_category_fn(recipes_path, categories_list):
    """
    Create a recipe category.
    User type the name of the category to be created
    :param recipes_path: main folder of the recipes
    :param categories_list: list of recipe categories
    """

    if len(categories_list) > 0:
        print("These are your recipe categories")
        for idx, cate in enumerate(categories_list):
            print(f"[{idx + 1}] {cate}")

    # enter name recipe category
    category_name = input("Type the new category name |>")
    category_name = '_'.join(category_name.split(' '))
    # print(category_name)
    new_category_path = Path(recipes_path, category_name)
    # create recipe category/folder
    try:
        # trying to create the category (folder)
        os.mkdir(new_category_path)
        print(f"{category_name} category has been created successfully in \n"
              f"{recipes_path}.\n")
    except FileExistsError:
        print(f"{category_name} already exists in {recipes_path}.")
    except Exception as e:
        print(f"An error has occurred: {str(e)}")


# Delete recipe category function
def delete_recipe_category_fn(recipes_path, categories_list):
    """
    Delete a recipe category.
    User type the name of the category to be deleted
    :param recipes_path: main folder of the recipes
    :param categories_list: list of recipe categories
    """
    category_name = recipe_category_selection(categories_list)
    category_path_to_rm = Path(
        recipes_path,
        category_name
    )

    # delete recipe category/folder
    try:
        # trying to delete the category (folder)
        Path(category_path_to_rm).rmdir()
        print(f"{category_name} category has been delete successfully from "
              f"{recipes_path}")
    except FileExistsError:
        print(f"{category_name} not exists in {recipes_path}.")
    except Exception as e:
        print(f"An error has occurred: {str(e)}")


def recipes_program():

    option_program: int = 1
    user_name = ''
    while option_program != 0:
        user, recipes_path = welcome_recipes(user_name, recipes_path_str)
        categories_list = [path.stem for path in Path(recipes_path).glob("**/*/")]

        if user_name == '':
            user_name = user_name + user
        option_program = 0
        if len(categories_list) == 0:
            print(f"{user_name} doesn't have recipe categories yet\n"
                  f"Please, create a recipe category first, \n"
                  f"then create a recipe for that category\n")
            # Create recipe category option
            option_program = option_program + 4
        else:
            option_program = recipe_options()

        match option_program:
            case 1:
                print("Read a recipe\n")
                read_recipe_fn(recipes_path, categories_list)
            case 2:
                print("Create a recipe\n")
                create_recipe_fn(recipes_path, categories_list)
            case 3:
                print("Delete a recipe\n")
                delete_recipe_fn(recipes_path, categories_list)
            case 4:
                print("Create recipe category\n")
                create_recipe_category_fn(recipes_path, categories_list)
            case 5:
                print("Delete a recipe category\n")
                delete_recipe_category_fn(recipes_path, categories_list)
            case 0:
                continue
        option_program = int(input("""[1] Main menu  [0] Exit\n|> """))
    print(f"Bye {user_name}")


recipes_program()
