import './App.css';
import NavAppBar from './components/Header/Header';
import Grid from "@mui/material/Grid";
import Body from "./components/Body/Body";


function App() {
    return (
        <Grid container justifyContent="center" height="100%">
            <NavAppBar/>
            <Body/>
        </Grid>
    );
}


export default App;
