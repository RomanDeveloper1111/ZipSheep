import React, {useEffect, useState} from "react";
import Button from '@mui/material/Button';

function Example() {
    const [count, setCount] = useState(0);

    useEffect(() =>{
        document.title = `Вы нажали ${count} раз.`;
    });

    return (
        <div>
            <p>Вы нажали {count} раз.</p>
            <Button variant="contained" onClick={() => setCount(count + 1)}>
                Нажми еще разик.
            </Button>
            <Button variant="contained" onClick={() => setCount(0)}>
                Сбросить счет
            </Button>
        </div>
    );
}

export default Example;

