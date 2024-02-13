import { createDrawerNavigator } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import Home from './components/Home/Home';
import Login from './components/User/Login';
import MyContext from './configs/MyContext';
import { useReducer } from 'react';
import MyUserReducer from './reducers/MyUserReducer';

const Drawer = createDrawerNavigator();

const App = () => {
  const [user, dispatch] = useReducer(MyUserReducer, null);

  return(
    <MyContext.Provider value={[user, dispatch]}>
      <NavigationContainer>
        <Drawer.Navigator>
          <Drawer.Screen name="Home" component={Home} options={{title: 'Trang chủ'}}/>
          <Drawer.Screen name="Login" component={Login} options={{title: 'Đăng nhập'}}/>
        </Drawer.Navigator>
      </NavigationContainer>
    </MyContext.Provider>
  )
}

export default App
