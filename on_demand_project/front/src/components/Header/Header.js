import * as React from 'react';
import AvatarMenu from './AvatarMenu';
import Typography from '@mui/material/Typography';
import Grid from "@mui/material/Grid";

export default function NavAppBar() {
  return (
    <Grid mt={1} mr={2}  ml={2} alignItems="center" container direction="row" justifyContent="space-between" className="headerBox">
        <Grid  item xs={6} >
            <Typography component="h6" variant="h5"  xs="6">
              Demand Delivery
          </Typography>
        </Grid>
        <Grid  container item justifyContent="flex-end" xs={6}>
            <AvatarMenu />
        </Grid>
    </Grid>
  );
}
