import * as http from "../http-common";
import IRecipeData from "../types/Recipe";

export async function getRecipes(): Promise<IRecipeData[] | undefined> {
    const response = await http.get("http://localhost:5000/recipes/");
      
    return !response.ok ? null : await response.json();
  }

// class RecipeDataService {
//     getall() {
//         return http.get<Array<IRecipeData>>("/recipes")
//     }

//     get(id: number) {
//         return http.get<IRecipeData>(`/recipes/${id}`)
//     }

//     create(data: IRecipeData) {
//         return http.post<IRecipeData>("/recipes", data)
//     }

//     update(data: IRecipeData, id: number) {
//         return http.put<any>(`/recipes/${id}`, data);
//       }
    
//       delete(id: number) {
//         return http.delete<any>(`/recipes/${id}`);
//       }
// }

// export default new RecipeDataService();
