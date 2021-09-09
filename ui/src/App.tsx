import React from 'react';

import { withStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import NativeSelect from '@material-ui/core/NativeSelect';
import InputBase from '@material-ui/core/InputBase';
import { Button, Grid } from "@material-ui/core";
import axios from "axios";
import SaveIcon from '@material-ui/icons/Save';
import {IRecommendation} from "./types/Recommendation";
import RecommendationItem from "./RecommendationItem";

import "./App.css"

const BootstrapInput = withStyles((theme) => ({
  root: {
    'label + &': {
      marginTop: theme.spacing(3),
    },
  },
  input: {
    borderRadius: 4,
    position: 'relative',
    backgroundColor: theme.palette.background.paper,
    border: '1px solid #ced4da',
    fontSize: 16,
    padding: '10px 26px 10px 12px',
    transition: theme.transitions.create(['border-color', 'box-shadow']),
    // Use the system font instead of the default Roboto font.
    fontFamily: [
      '-apple-system',
      'BlinkMacSystemFont',
      '"Segoe UI"',
      'Roboto',
      '"Helvetica Neue"',
      'Arial',
      'sans-serif',
      '"Apple Color Emoji"',
      '"Segoe UI Emoji"',
      '"Segoe UI Symbol"',
    ].join(','),
    '&:focus': {
      borderRadius: 4,
      borderColor: '#80bdff',
      boxShadow: '0 0 0 0.2rem rgba(0,123,255,.25)',
    },
  },
}))(InputBase);

function App() {
  const [recommendations, setRecommendations] = React.useState<IRecommendation[]>([]);
  const [category, setCategory] = React.useState('movies');
  const [title, setTitle] = React.useState('');
  const handleCategoryChange = (event: any) => {
    console.log(event.target.value);
    setCategory(event.target.value);
  };

  const handleTitleChange = (event: any) => {
    setTitle(event.target.value);
  };

  const handleSubmit = async () => {
    const request = {
      'title': title,
      'category': category
    }

    const { data } = await axios.post<IRecommendation[]>("http://127.0.0.1:5000/api/recommend", request)
    console.log(data)
    setRecommendations(data)
  };

  return (
    <div className={"App"}>
      <Grid
        container
        spacing={0}
        direction="row"
        justifyContent="center"
        style={{ minHeight: '100px' }}
      >
        <Grid item>
          <FormControl className={"margin"}>
            <InputLabel htmlFor="demo-customized-textbox">Title</InputLabel>
            <BootstrapInput id="demo-customized-textbox" onChange={handleTitleChange}/>
          </FormControl>
        </Grid>

        <Grid item alignItems="flex-start" style={{ display: "flex" }}>
          <FormControl className={"margin"}>
            <InputLabel htmlFor="demo-customized-select-native">Category</InputLabel>
              <NativeSelect
                id="demo-customized-select-native"
                value={category}
                onChange={handleCategoryChange}
                input={<BootstrapInput />}
              >
                <option value={'None'}/>
                <option value={"movies"}>Филм</option>
                <option value={"books"}>Книга</option>
              </NativeSelect>
          </FormControl>
        </Grid>
        <Grid item alignItems="flex-start" style={{ display: "flex" }}>
          <FormControl className={"margin"}>
            <Button
                variant="contained"
                color="primary"
                size="large"
                className={"submit"}
                startIcon={<SaveIcon />}
                onClick={handleSubmit}
              >
                Submit
              </Button>
          </FormControl>
        </Grid>

      </Grid>
      <div className={"root"}>
        <Grid container spacing={2} direction="row" justify="flex-start" alignItems="flex-start">
                {recommendations.map(recommendation => (
                    <RecommendationItem recommendation={recommendation}
                                        recommendation_index={recommendations.indexOf(recommendation)}
                                        key={recommendations.indexOf(recommendation)}
                    />
                ))}
            </Grid>
      </div>
    </div>
  );
}

export default App;
