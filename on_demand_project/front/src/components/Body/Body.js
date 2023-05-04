import {FormControl, FormHelperText} from "@mui/material";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import Typography from "@mui/material/Typography";

export default function Body(){
    return (
        <Grid container height="90%">
            <Grid justifyContent="center" p={3} m={6} item xs={6} border="1px solid black" borderRadius={5} height="90%">
                {/*Forms*/}
                <FormControl >
                    <Typography> Ordering</Typography>
                    <TextField id="outlined-basic" label="Outlined" variant="outlined" />
                    <TextField id="outlined-basic" label="Outlined" variant="outlined" />
                </FormControl>
            </Grid>
            <Grid m={6} item xs={6}>
                {/*Map*/}
            </Grid>
        </Grid>
    )
}