import IRecipeData from "../types/Recipe"
import { FC } from 'react';
import RecipeCard from "./Recipe";
import { Col, Container, Row } from "react-bootstrap";

interface RecipeListProps {
    recipes: IRecipeData[];
}

const RecipeList: FC<RecipeListProps> = ({ recipes }) => {
    return (
        <Container>
            <h3 className='headline'>Latest Recipes</h3>
            <span className="line rb margin-bottom-35"></span>
            <Row lg={3}>
                { recipes?.map((recipe) => (
                    <Col key={recipe.id} className="d-flex">
                        <RecipeCard recipe={recipe} />
                    </Col>
                )) }
            </Row>
        </Container>
    )
}

export default RecipeList;