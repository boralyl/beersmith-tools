import sys

from pybeerxml import Parser


LITERS_TO_GALLON = 0.2641720524


def liters_to_gallons(liters: float) -> float:
    return round(liters * LITERS_TO_GALLON, 2)


def hop_use(use: str) -> str:
    if use == "Aroma":
        return "Steep/Whirlpool."
    return use


def main(beer_xml_path: str):
    parser = Parser()
    recipe = parser.parse(beer_xml_path)[0]
    ingredients_rows = []
    for f in recipe.fermentables:
        ingredients_rows.append(f"|{f.display_amount}|{f.name}|{f.type}|")
    for h in recipe.hops:
        ingredients_rows.append(
            f"|{h.display_amount}|{h.name} [{h.alpha}%] - {hop_use(h.use)} {h.display_time}|Hop|"
        )
    for y in recipe.yeasts:
        ingredients_rows.append(
            f"|1 pkg|{y.name} ({y.laboratory}#{y.product_id})|Yeast|"
        )
    ingredients = "\n".join(ingredients_rows)

    mash_steps = []
    for step in recipe.mash.steps:
        mash_steps.append(
            f"|{step.name}|{step.description}|{step.display_step_temp}|{step.step_time} mins|"
        )
    mash_step_str = "\n".join(mash_steps)
    md = f"""
**Name**: {recipe.name}<br />
**Style**: {recipe.style.name} ({int(recipe.style.category_number)}{recipe.style.style_letter})<br />
**Type**: {recipe.type}

## Recipe Specifications
**Boil Size**: {recipe.display_boil_size}<br />
**Batch Size (fermenter)**: {recipe.display_batch_size}<br />
**Estimated OG**: {recipe.est_og}<br />
**Estimated Color**: {recipe.est_color}<br />
**Estimated IBU**: {round(recipe.ibu, 2)} ({recipe.ibu_method})<br />
**Estima.ed ABV**: {recipe.est_abv}<br />
**Brewhouse Efficiency**: {recipe.efficiency}%<br />
**Boil Time**: {int(recipe.boil_time)} minutes<br />

## Ingredients
|Amount|Name|Type|
|-|-|-|
{ingredients}

## Mash

**Mash Schedule**: Single Infusion, Light Body, Batch Sparge

|Name|Description|Step Temperature|Step Time|
|-|-|-|-|
{mash_step_str}
    """
    return md


if __name__ == "__main__":
    print(main(sys.argv[1]))
