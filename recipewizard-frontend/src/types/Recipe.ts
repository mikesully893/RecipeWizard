import IRecipeIngredientData from "./Ingredient";

export default interface IRecipeData {
    id: number,
    name: string,
    prep_time: string,
    servings: number,
    calories: number,
    ingredients: IRecipeIngredientData[],
    steps: JSON
}