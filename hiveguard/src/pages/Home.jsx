import Header from "../components/Header";
import { Link } from "react-router-dom"

export default function Home() {

    return (
        <>
            <Header/>
            <h2>Simply The Bee's Knees</h2>
            <Link to='/beemonitor'><button class="button-28" role="button">Hive Data</button></Link> 
        </>
    )
}