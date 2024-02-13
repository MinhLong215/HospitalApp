import { View, Text, TextInput } from "react-native"
import MyStyles from "../../styles/MyStyles"
import Style from "./Style"
import { TouchableOpacity } from "react-native-gesture-handler"
import { useContext, useState } from "react"
import MyContext from "../../configs/MyContext"


const Login = () => {
    const [username, setUsername] = useState();
    const [password, setPassword] = useState();
    const [user, dispatch] = useContext(MyContext);

    const login = () => {
        if(username === 'admin' && password === '123456'){
            dispatch({
                type: "login",
                payload: {
                    "username": 'admin'
                }
            })
        }
    }

    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.title}>ĐĂNG NHẬP</Text>

            <TextInput value={username} onChangeText={t => setUsername(t)} style={Style.input} placeholder="Tên đăng nhập..." />
            <TextInput secureTextEntry={true} value={password} onChangeText={t => setPassword(t)} style={Style.input} placeholder="Mật khẩu..." />
            <TouchableOpacity onPress={login}>
                <Text style={Style.button}>Đăng nhập</Text>
            </TouchableOpacity>
        </View>
    )
}

export default Login