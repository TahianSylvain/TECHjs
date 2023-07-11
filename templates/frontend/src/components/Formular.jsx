import React from 'react';
import './Formular.css';
// import { send } from 'process';


class Formular extends React.Component {
    constructor(props) {
        super(props)
        this.state = { 
            name: '',
            deadline: '',
            reminder: '',
            description: '',
        }
        this.handlechange = this.handlechange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    
    handlechange(e){
        const name = e.target.name;
        this.setState({
            [name]: e.target.value,
        })
        console.log(this.state)
    }
    handleSubmit(e){
        e.preventDefault()
        const data = JSON.stringify(this.state);
        console.log(data);
        
        // Send the fucking new data
        

        this.setState({
            name: '',
            deadline: '',
            reminder: '',
            description: '',
        })
        
    }

    render() {
        return <form className="signup-form" action='' encType='text/plain' method='POST' onSubmit={this.handleSubmit}>
            <div className="form-header">
                <h1>New Notation for "YOUR NAME"</h1>
                Your name
            </div>
        
            <div className="form-body">
                <label htmlFor="name">Name</label>
                <input type="text" name='name' value={this.state.name} onChange={this.handlechange}/>

                <label htmlFor="deadline">Timing</label>
                <input type='datetime-local' name="deadline" id="temps" value={this.state.deadline} onChange={this.handlechange}/>

                <label htmlFor="reminder">reminding</label>
                <input type="time" name="reminder" id="rappel" value={this.state.reminder} onChange={this.handlechange}/>

                <label htmlFor="description">Description</label>
                <textarea name="description" id="decrire" cols="30" rows="10" value={this.state.description} onChange={this.handlechange}></textarea>
            </div>
            <div className="form-footer">
                <button type="reset">Undo</button>
                <button type="submit">Send</button>
            </div>
        </form>
    }
}

export default Formular;
