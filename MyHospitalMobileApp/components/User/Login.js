import { View, Text, TextInput, ActivityIndicator } from "react-native"
import MyStyles from "../../styles/MyStyles"
import Style from "./Style"
import { TouchableOpacity } from "react-native-gesture-handler"
import { useContext, useState } from "react"
import MyContext from "../../configs/MyContext"
import API, { authApi, endpoints } from "../../configs/API"


const Login = ({navigation}) => {
    const [username, setUsername] = useState();
    const [password, setPassword] = useState();
    const [loading, setLoading] = useState(false);
    const [user, dispatch] = useContext(MyContext);

    const login = async () => {
        setLoading(true);

        try{
            console.log(endpoints['login']);
            let res = await API.post(endpoints['login'], {
                "username": username,
                "password": password,
                "client_id": "Yybp9Jtk4W8oByYuVnGL4bfdmIk6iKJX4Qgubp7L",
                "client_secret": "WnEiWm72c5mguFMyKoDk6bTlLYkZw9vit6AMo9tRfxN6tOvohk08h0ioskEoLJ0Sp3YEnDl0Z1E7872Zaj20cyKXwLqO012NOAeobsFyFbb4AjA3C6TKmbSrFHXXdOwh",
                "grant_type": "password"
            })
            console.info(res.data)

            let user = await authApi(res.data.access_token).get(endpoints['current-user']);
            dispatch({
                type: "login",
                payload: user.data
            })
            navigation.navigate("Home");
        }catch (ex){
            console.error(ex);
        }finally{
            setLoading(false);
        }
        // if(username === 'admin' && password === '123456'){
        //     dispatch({
        //         type: "login",
        //         payload: {
        //             "username": 'admin'
        //         }
        //     })
        // }
    }

    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.title}>ĐĂNG NHẬP</Text>

            <TextInput value={username} onChangeText={t => setUsername(t)} style={Style.input} placeholder="Tên đăng nhập..." />
            <TextInput secureTextEntry={true} value={password} onChangeText={t => setPassword(t)} style={Style.input} placeholder="Mật khẩu..." />

            {loading===true?<ActivityIndicator />:<>
                <TouchableOpacity onPress={login}>
                    <Text style={Style.button}>Đăng nhập</Text>
                </TouchableOpacity>
            </>}
        </View>
    )
}

export default Login