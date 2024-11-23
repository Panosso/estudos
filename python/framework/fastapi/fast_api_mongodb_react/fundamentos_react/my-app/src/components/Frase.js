import styles from "./Frases.module.css"

function Frase(){
    return (
        <div className={styles.fraseContainer}>
            <h3 className={styles.fraseContent}>Melhor forma de ganhar grana é estudar</h3>
        </div>
    )
}

export default Frase