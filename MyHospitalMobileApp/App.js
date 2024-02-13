import { createDrawerNavigator } from '@react-navigation/drawer';
import { NavigationContainer } from '@react-navigation/native';
import Home from './components/Home/Home';
import Login from './components/User/Login';

const Drawer = createDrawerNavigator();

const App = () => {
  return(
    <NavigationContainer>
      <Drawer.Navigator>
        <Drawer.Screen name="Home" component={Home} />
        <Drawer.Screen name="Login" component={Login}/>
      </Drawer.Navigator>
    </NavigationContainer>
  )
}

export default App
