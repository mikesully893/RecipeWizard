import { FC } from 'react';
import React, { useEffect, useState, useContext } from "react";
import IRecipeData from '../types/Recipe';
import { getRecipes } from '../services/recipe-service';
import RecipeList from '../components/RecipeList';


const HomePage: FC = () => {
    const [recipes, setRecipes] = useState<IRecipeData[]>();

    useEffect(() => {
        getRecipes()
        .then((recipes) => {setRecipes(recipes)});
    }, []);

    return (
        <div>
            {recipes && <RecipeList recipes={recipes}/>}
        </div>
    );
};

export default HomePage;

