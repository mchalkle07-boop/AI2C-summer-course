# problem 1
class Soldier:
    """Represents a soldier with rank, fitness, and deployment status."""

    def __init__(self, name: str, rank: str, fitness: int, deployed: bool):
        self.name = name
        self.rank = rank
        self.fitness = fitness
        self.deployed = deployed

    def dispatch(self) -> None:
        """Mark this soldier as deployed."""
        self.deployed = True

    def __str__(self) -> str:
        return f"{self.name} ({self.rank}, fitness: {self.fitness}, deployed: {self.deployed})"


def process_reports(report_list: list[str]) -> tuple[dict[str, Soldier], set[str]]:
    """Parse report strings and return (roster_dict, ranks_set)."""
    roster: dict[str, Soldier] = {}
    ranks: set[str] = set()

    for report in report_list:
        parts = report.split("|")

        name = parts[0].strip().title()
        rank = parts[1].strip().upper()

        fitness_str = parts[2].strip().split(":")[1]
        fitness = int(fitness_str)

        status = parts[3].strip().split(":")[1].lower()
        deployed = status == "deployed"

        soldier = Soldier(name, rank, fitness, deployed)
        roster[name] = soldier
        ranks.add(rank)

    return roster, ranks


def show_available(roster: dict[str, Soldier]) -> None:
    """Display all available soldiers, sorted alphabetically."""
    available_names = [name for name, soldier in roster.items() if not soldier.deployed]
    available_names.sort()
    print(f"Available soldiers: {available_names}")


def dispatch(roster: dict[str, Soldier], name: str) -> None:
    """Dispatch a soldier by name, or print an error if not available."""
    print(f"Dispatching {name}...", end=" ")
    soldier = roster.get(name)
    if soldier is None:
        print(f"{name} not found.")
        return

    if soldier.deployed:
        print(f"{name} is already deployed.")
        return

    soldier.dispatch()
    print("Done. Status set to deployed.")


def fitness_report(roster: dict[str, Soldier]) -> dict[str, list[str]]:
    """Return a dict with 'high', 'medium', 'low' fitness bands."""
    report = {"high": [], "medium": [], "low": []}

    for name, soldier in roster.items():
        if soldier.fitness >= 80:
            report["high"].append(name)
        elif soldier.fitness >= 60:
            report["medium"].append(name)
        else:
            report["low"].append(name)

    for band in report:
        report[band].sort()

    print("=== FITNESS REPORT ===")
    print(f"High (>=80):   {report['high']}")
    print(f"Medium (60-79): {report['medium']}")
    print(f"Low (<60):     {report['low']}")

    return report


# problem 2
class Recipe:
    """Represents a recipe with a name and list of ingredients."""

    def __init__(self, name: str, ingredients: list[str]):
        self.name = name
        self.ingredients = ingredients

    def can_make(self, pantry_set: set[str]) -> bool:
        """Check if all ingredients are in the pantry."""
        return all(ingredient in pantry_set for ingredient in self.ingredients)

    def missing_ingredients(self, pantry_set: set[str]) -> list[str]:
        """Return sorted list of missing ingredients."""
        missing = [ing for ing in self.ingredients if ing not in pantry_set]
        return sorted(missing)


class Pantry:
    """Represents a pantry with a set of ingredients."""

    def __init__(self, items: list[str]):
        self.items = set(items)

    def add_ingredients(self, extra_ingredients: list[str]) -> None:
        """Add new ingredients to the pantry."""
        self.items.update(extra_ingredients)

    def has(self, ingredient: str) -> bool:
        """Check if the pantry contains an ingredient."""
        return ingredient in self.items

    def get_items(self) -> set[str]:
        """Return the set of all items in the pantry."""
        return self.items


def create_recipes(recipe_data: dict[str, list[str]]) -> list[Recipe]:
    """Convert recipe dictionary to list of Recipe objects."""
    recipes = []
    for name, ingredients in recipe_data.items():
        recipes.append(Recipe(name, ingredients))
    return recipes


def check_recipes(recipes: list[Recipe], pantry: Pantry) -> None:
    """Check which recipes can be made and print results."""
    print("=== RECIPE CHECKER ===")
    pantry_set = pantry.get_items()
    all_ingredients = set()

    for recipe in recipes:
        all_ingredients.update(recipe.ingredients)
        if recipe.can_make(pantry_set):
            print(f"{recipe.name:<14} : CAN MAKE")
        else:
            missing = recipe.missing_ingredients(pantry_set)
            print(f"{recipe.name:<14} : MISSING -- {missing}")

    sorted_all = sorted(all_ingredients)
    print(f"\nAll unique ingredients ({len(sorted_all)}): {sorted_all}")


# problem 3
class LyricAnalyzer:
    """Analyzes song lyrics for word frequency."""

    def __init__(self, lyrics: str):
        self.lyrics = lyrics
        cleaned = lyrics.lower()
        for punctuation in [",", ".", "!", "?", '"', "'", ";", ":"]:
            cleaned = cleaned.replace(punctuation, "")
        self.words = cleaned.split()

    def count_words(self) -> dict[str, int]:
        """Return dictionary mapping words to their counts."""
        counts = {}
        for word in self.words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts

    def unique_word_count(self) -> int:
        """Return the number of unique words."""
        return len(set(self.words))

    def most_common_word(self) -> tuple[str, int]:
        """Return (word, count) for the most frequent word."""
        counts = self.count_words()
        best_word = max(counts, key=counts.get)
        return (best_word, counts[best_word])

    def print_report(self) -> None:
        """Print complete word analysis report."""
        print("=== WORD COUNT ===")
        counts = self.count_words()
        for word in sorted(counts):
            print(f"{word:<10} : {counts[word]}")

        unique = self.unique_word_count()
        word, count = self.most_common_word()

        print(f"\nUnique words: {unique}")
        print(f"Most common word: '{word}' — {count} times")

    def filter_stopwords(self, stop_words: set[str]) -> None:
        """Remove stop words from the word list."""
        self.words = [word for word in self.words if word not in stop_words]


# problem 4
class Animal:
    """Represents a zoo animal with species, age, and origin."""

    def __init__(self, name: str, species: str, age: int, origin: str):
        self.name = name
        self.species = species
        self.age = age
        self.origin = origin

    def __str__(self) -> str:
        return f"{self.name} ({self.species}, {self.age} years, from {self.origin})"

    def get_info(self) -> None:
        """Print detailed information about the animal."""
        print(f"Name:    {self.name}")
        print(f"Species: {self.species}")
        print(f"Age:     {self.age}")
        print(f"Origin:  {self.origin}")


def build_registry(raw_data: list[str]) -> dict[str, Animal]:
    """Parse raw data strings and return dictionary of Animal objects."""
    registry: dict[str, Animal] = {}

    for entry in raw_data:
        parts = entry.split(",")
        name = parts[0].strip()
        species = parts[1].strip()
        age = int(parts[2].strip())
        origin = parts[3].strip()

        animal = Animal(name, species, age, origin)
        registry[name] = animal

    return registry


def analyze_registry(registry: dict[str, Animal]) -> None:
    """Analyze and print statistics about the zoo registry."""
    print("=== ZOO REGISTRY BUILT ===")
    print(f"{len(registry)} animals registered.\n")

    species_set = {animal.species for animal in registry.values()}
    origin_set = {animal.origin for animal in registry.values()}

    print(f"Unique species: {species_set}")
    print(f"Animals come from {len(origin_set)} distinct regions.")


def group_by_species(registry: dict[str, Animal]) -> dict[str, list[Animal]]:
    """Group animals by species and return the groupings."""
    groups: dict[str, list[Animal]] = {}

    for animal in registry.values():
        if animal.species not in groups:
            groups[animal.species] = []
        groups[animal.species].append(animal)

    return groups


# This will only execute if this script is executed directly, not imported
if __name__ == "__main__":
    # you can use this variable to test problems independently
    # while you're working locally
    TESTING_PROBLEM = 1

    if TESTING_PROBLEM == 1:
        reports = [
            "SANTOS | Private | Fitness:91 | Status:available",
            "KOWALSKI | Corporal | Fitness:74 | Status:deployed",
            "OKAFOR | Sergeant | Fitness:88 | Status:available",
            "BRIGGS | Private | Fitness:55 | Status:available",
            "NAKAMURA | Corporal | Fitness:82 | Status:deployed",
            "REYES | Sergeant | Fitness:79 | Status:available",
        ]

        roster, ranks = process_reports(reports)

        print("=== ROSTER LOADED ===")
        print(f"{len(roster)} soldiers on record.")
        print(f"Ranks on file: {ranks}\n")

        show_available(roster)
        print()

        dispatch(roster, "Santos")
        dispatch(roster, "Kowalski")

        print("\nUpdated status:")
        for n in ["Santos", "Kowalski"]:
            s = roster[n]
            status = "deployed" if s.deployed else "available"
            print(f"  {n:<8} : {status}")

        print()
        fitness_report(roster)

    elif TESTING_PROBLEM == 2:
        recipe_data = {
            "omelette": ["eggs", "butter", "salt", "pepper", "cheese"],
            "pancakes": ["flour", "eggs", "milk", "butter", "sugar", "salt"],
            "tomato pasta": [
                "pasta",
                "tomatoes",
                "garlic",
                "olive oil",
                "salt",
                "pepper",
            ],
            "grilled cheese": ["bread", "cheese", "butter"],
        }
        pantry_items = [
            "eggs",
            "butter",
            "salt",
            "pepper",
            "cheese",
            "milk",
            "bread",
            "garlic",
        ]

        recipes = create_recipes(recipe_data)
        pantry = Pantry(pantry_items)

        # Record which recipes could be made BEFORE the shopping trip
        before = {r.name for r in recipes if r.can_make(pantry.get_items())}

        check_recipes(recipes, pantry)

        raw_input_str = input("\nEnter extra ingredients (comma-separated): ")
        extras = [item.strip() for item in raw_input_str.split(",") if item.strip()]
        pantry.add_ingredients(extras)

        print("\n=== AFTER SHOPPING ===")
        check_recipes(recipes, pantry)

        after = {r.name for r in recipes if r.can_make(pantry.get_items())}
        newly_available = sorted(after - before)

        if newly_available:
            print(f"\nNewly available recipes: {newly_available}")
        else:
            print("\nNo new recipes became available.")

    elif TESTING_PROBLEM == 3:
        lyrics = """
we will we will rock you
we will we will rock you
buddy youre a boy make a big noise
playing in the street gonna be a big man someday
you got mud on your face you big disgrace
kicking your can all over the place singing
we will we will rock you
"""
        analyzer = LyricAnalyzer(lyrics)
        analyzer.print_report()

        stop_words = {"a", "the", "you", "your", "in", "on", "we", "be", "got"}
        analyzer.filter_stopwords(stop_words)

        print("\n=== AFTER REMOVING STOPWORDS ===")
        analyzer.print_report()

    elif TESTING_PROBLEM == 4:
        raw_data = [
            "Simba, lion, 7, Africa",
            "Pebbles, penguin, 3, Antarctica",
            "Kovu, lion, 4, Africa",
            "Bubbles, dolphin, 12, Ocean",
            "Mango, parrot, 6, South America",
            "Nala, lion, 5, Africa",
            "Splash, dolphin, 8, Ocean",
            "Crackers, parrot, 2, South America",
        ]

        registry = build_registry(raw_data)
        analyze_registry(registry)

        raw_name = input("\nEnter an animal name to look up: ")
        name = raw_name.strip().title()

        animal = registry.get(name)
        print()
        if animal is None:
            print(f"{name} not found.")
        else:
            animal.get_info()

        print("\n=== GROUPED BY SPECIES ===")
        groups = group_by_species(registry)
        for species, animals in groups.items():
            names = [a.name for a in animals]
            print(f"{species:<8}: {', '.join(names)}")

    else:
        print("There are only 4 problems!")