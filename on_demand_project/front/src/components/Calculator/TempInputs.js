import {Component} from "react";

const scaleNames = {
    c: 'Цельсия',
    f: 'Фаренгейта'
}
class TempInputs extends Component{
    constructor(props) {
        super(props);
        this.handleChangeInput = this.handleChangeInput.bind(this);
    }
    handleChangeInput(e){
        this.props.onTemperatureChange(e.target.value);
    }
    render(){
        return(
            <fieldset>
                <legend>Введите температуру в градусах {scaleNames[this.props.scaleName]}</legend>
                <input type="number"
                    value={this.props.temperature}
                    onChange={this.handleChangeInput}
                />

            </fieldset>
        );
    }

}

export default TempInputs;