import { FC } from 'react';
import { Container, Navbar } from 'react-bootstrap';

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
      </Container>
    </Navbar>
  );
};
export default Header;