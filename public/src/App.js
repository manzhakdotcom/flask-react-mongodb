import React, {Component} from 'react';
import axios from 'axios';

class App extends Component{
    state = {
            locations: []
    };

    componentDidMount() {
        axios.get('http://localhost:5000')
            .then(resp => resp.data)
            .then(data => {
                this.setState({ locations: data })
            });
    }

    render() {
        return (
            this.state.locations.map((location) =>
                <ul key={location.id}>
                    <li>{location.state}</li>
                    <li>{location.city}</li>
                    <li>{location.pop}</li>
                </ul>
            )
        )

    }

}

export default App;
