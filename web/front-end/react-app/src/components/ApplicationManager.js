import React, { Component } from 'react';
import NavBarComponent from "./NavBarComponent";
import SearchByUsernameComponent from "./SearchByUsernameComponent";
import TweetContainer from "./TweetContainer";
import MadeWLoveComponent from './MadeWLoveComponent';

class ApplicationManager extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        }
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        console.log('Updated');
    }

    updateData = (freshData) => {
        this.setState({
            data : freshData
        });
    };

    render() {
        return (
            <div>
                <NavBarComponent/>
                <SearchByUsernameComponent updateCallback={this.updateData}/>
                <TweetContainer data={this.state.data}/>
                <MadeWLoveComponent/>
            </div>
        );
    }
}

export default ApplicationManager;