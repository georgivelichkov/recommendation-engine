import React from 'react';
import {Button, Card, CardActionArea, CardActions, CardContent, CardMedia, Grid, Typography} from "@material-ui/core";
import {IRecommendation} from "./types/Recommendation";

import "./App.css"

interface Props{
    recommendation: IRecommendation
    recommendation_index: number
}

export default function RecommendationItem(props: Props) {
    return (
        <Grid item xs={12} sm={6} md={3}>
            <Card className={"card"}>
              <CardActionArea>
                <CardMedia
                  className={"media"}
                  image={props.recommendation.image_url}
                  title={props.recommendation.title}
                />
                <CardContent>
                  <Typography gutterBottom variant="h5" component="h2">
                    {props.recommendation.title}
                  </Typography>
                  <Typography variant="body2" color="textSecondary" component="p">
                    Release Date: {props.recommendation.year}
                  </Typography>
                </CardContent>
              </CardActionArea>
              <CardActions>
                <Button size="small" color="primary">
                  <a href={props.recommendation.homepage} className={"link"}>Go to homepage</a>
                </Button>
              </CardActions>
            </Card>
        </Grid>
    )
}
