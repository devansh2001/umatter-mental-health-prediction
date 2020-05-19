import React, { Component } from 'react';

class MadeWLoveComponent extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <h4 className={'made-with-love'}>
                        Made with ♥ by Devansh Jatin Ponda
                </h4>
            </div>
        );
    }
}

export default MadeWLoveComponent;