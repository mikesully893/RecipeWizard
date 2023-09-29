import { FC } from 'react';
import Carousel from 'react-bootstrap/Carousel';

const RecipeCarousel: FC = () => {
    return (
        <Carousel className='recipe-carousel'>
            <Carousel.Item className='recipe-carousel-item'>
                <Carousel.Caption className='recipe-carousel-caption'>
                    <h5>First slide</h5>
                    <p>This will contain some info about the recipe</p>
                </Carousel.Caption>
                <img
                    className='d-block w-100 recipe-carousel-image'
                    src='/sample_images/burrito_bowl.jpg'
                    alt='First Slide' 
                />
            </Carousel.Item>
            <Carousel.Item className='recipe-carousel-item'>
                <img
                    className='d-block w-100 recipe-carousel-image'
                    src='/sample_images/beef.jpg'
                    alt='First Slide' 
                />
                <Carousel.Caption className='recipe-carousel-caption'>
                    <h5>Second slide</h5>
                    <p>This will contain some info about the recipe</p>
                </Carousel.Caption>
            </Carousel.Item>
        </Carousel>
    )
}

export default RecipeCarousel;