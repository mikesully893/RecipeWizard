import { FC } from 'react';
import Header from './components/Header';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import HomePage from './pages/HomePage';

const App: FC = () => {
  return (
    <div className='App'>
      <Header />
        <main className='container'>
          <Routes>
            <Route path='/' element={ <HomePage /> }/>
          </Routes>
        </main>
    </div>
  );
}

// function App() {
//   return (
//     <div className='App'>
//       <Header />
//     </div>
//   );
// }
export default App;

// import React, { Component } from "react";
// import { Switch, Route, Link } from "react-router-dom";
// import "bootstrap/dist/css/bootstrap.min.css";
// import "./App.css";

// import CreateRecipe from "./components/CreateRecipe";
// import Recipe from "./components/Recipe";
// import RecipeList from "./components/RecipeList";

// class App extends Component {
//   render() {
//     return (
//       <div>
//         <nav className="navbar navbar-expand navbar-dark bg-dark">
//           <Link to={"/recipes"} className="nav-brand">
//             RecipeWizard
//           </Link>
//           <li className="nav-item">
//             <Link to={"/recipes"} className="nav-link">
//               Recipes
//             </Link>
//           </li>
//           <li className="nav-item">
//             <Link to={"/create"} className="nav-link">
//               Create
//             </Link>
//           </li>
//         </nav>

//         <div className="container mt-3">
//           <Switch>
//             <Route exact path={["/", "/recipes"]} component={RecipeList} />
//             <Route exact path={"/add"} component={CreateRecipe} />
//             <Route exact path={"/recipes/:id"} component={Recipe} />
//           </Switch>
//         </div>
//       </div>
//     );
//   }
// }

// export default App;
