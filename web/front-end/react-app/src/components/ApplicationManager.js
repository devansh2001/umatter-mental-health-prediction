import React, { Component } from 'react';
import NavBarComponent from "./NavBarComponent";
import SearchByUsernameComponent from "./SearchByUsernameComponent";
import TweetContainer from "./TweetContainer";

class ApplicationManager extends Component {
    constructor(props) {
        super(props);
        this.state = {
            data: []
        }
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
                <TweetContainer/>
            </div>
        );
    }
}

export default ApplicationManager;