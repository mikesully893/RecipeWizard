import IRecipeData from "../types/Recipe"
import { FC } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import './style.css';
import { FaRegClock } from "react-icons/fa";
import { GiKnifeFork } from "react-icons/gi";


interface RecipeCardProps {
    recipe: IRecipeData;
}

const RecipeCard: FC<RecipeCardProps> = ({ recipe }) => {

    return (
        <Card className="bg-light text-dark flex-fill recipe-card" style={{ width: '18rem' }}>
            <Card.Img src="/sample_images/burrito_bowl.jpg" alt="Card Image" className="recipe-card-image"/>
            <Card.Body>
                <Card.Title className="recipe-card-title">{ recipe.name }</Card.Title>
                <div>
                    <span><Card.Text><FaRegClock /> { recipe.prep_time }</Card.Text></span>
                    <span><Card.Text><GiKnifeFork /> { recipe.servings }</Card.Text></span>
                </div>
            </Card.Body>
        </Card>
    )
}

export default RecipeCard;
