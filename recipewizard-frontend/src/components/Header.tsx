import { FC } from 'react';
import { Container, Navbar, Nav } from 'react-bootstrap';

const Header: FC = () => {
  return (
    <Navbar className="recipes-navbar">
      <Container>
        <Navbar.Brand>
          <img 
            src='/logo/RecipeWizard-logos.jpeg'
            width='110'
            height='110'
            className='d-inline-block align-top'
            alt='RecipeWizard'
          />
        </Navbar.Brand>
        <Nav className="me-auto">
          <Nav.Link href='#home'>Home</Nav.Link>
          <Nav.Link href='#recipes'>Recipes</Nav.Link>
          <Nav.Link href='#submit'>Submit Recipe</Nav.Link>
        </Nav>
      </Container>
    </Navbar>
  );
};
export default Header;