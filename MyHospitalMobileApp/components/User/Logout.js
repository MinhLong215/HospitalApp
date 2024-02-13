import { useContext } from "react"
import { Button } from "react-native"
import MyContext from "../../configs/MyContext"

const Logout = () => {
    const[user, dispatch] = useContext(MyContext);

    const logout = () => {
        dispatch({
            "type": "logout"
        })
    }

    return <Button title="Đăng xuất" onPress={logout}/>
}

export default Logout