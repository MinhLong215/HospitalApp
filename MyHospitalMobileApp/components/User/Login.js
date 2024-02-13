import { View, Text, TextInput } from "react-native"
import MyStyles from "../../styles/MyStyles"
import Style from "./Style"


const Login = () => {
    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.title}>ĐĂNG NHẬP</Text>

            <TextInput style={Style.input} placeholder="Tên đăng nhập..." />
            <TextInput style={Style.input} placeholder="Mật khẩu..." />
        </View>
    )
}

export default Login