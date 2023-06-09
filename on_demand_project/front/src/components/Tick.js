import ReactDOM from "react-dom/client";
import React from "react";

class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = {date: new Date()};
    }

    componentDidMount() {
        this.timerID = setInterval(
            () => this.tick(),
            1000
        )
    }
    componentWillUnmount() {
        clearInterval(this.timerID)
    }

    tick(){
        this.setState({
            date: new Date()
        });
    }
    render(){
        return(
            <h2>Сейчас {this.state.date.toLocaleTimeString()}.</h2>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Clock />);

export default Clock;