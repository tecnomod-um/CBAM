import MainWindow from './components/MainWindow/MainWindow'
import './App.css';
import { StyledEngineProvider } from '@mui/material/styles';


function App() {

  return (
    <StyledEngineProvider injectFirst>
      <div className="App">
        <MainWindow />
      </div>
    </StyledEngineProvider>
  );
}

export default App;
