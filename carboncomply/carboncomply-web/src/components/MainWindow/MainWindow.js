import { React, useState } from "react";
import Container from '@mui/material/Container';
import DownloadableXMLBox from '../DownloadableXMLBox/DownloadableXMLBox';
import DownloadableTTLBox from '../DownloadableTTLBox/DownloadableTTLBox';
import { MuiFileInput } from 'mui-file-input'
import LoadingButton from '@mui/lab/LoadingButton';
import SendIcon from '@mui/icons-material/Send';
import Stack from '@mui/material/Stack';
import MainWindowStyles from './MainWindow.module.css';
import * as Config from '../../Config';
import axios from 'axios';
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';
import RDFGraph from '../RDFGraph/RDFGraph';

function MainWindow() {
  const [files, setFiles] = useState([]);
  const [xmlText, setXmlText] = useState('');
  const [ttlText, setTtlText] = useState('');
  const [processing, setProcessing] = useState(false);
  const [activeTab, setActiveTab] = useState('xml');

  const handleChange = (newFiles) => {
    setFiles(newFiles)
  }

  async function handleProcess() {
    setProcessing(true);
    let formData = new FormData();
    files.forEach((file) => formData.append('cbam_xls', file));
    //formData.append('cbam_xls', files);
    axios.post(Config.POST_CONVERT_URL, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }).then(response => {
      setXmlText(response.data.xml);
      setTtlText(response.data.rdf);
      setProcessing(false);
    }).catch(error => {
      console.log(error);
      setXmlText('');
      setTtlText('');
      setProcessing(false);
    });
    
  }

  const handleChangeTab = (event, newValue) => {
    setActiveTab(newValue);
  };


  return (
    <Container >
      <Stack spacing={1} alignItems={'center'}>
        <MuiFileInput multiple value={files} onChange={handleChange} />
        <LoadingButton
          disabled={files === null || files.length === 0}
          size="large"
          onClick={handleProcess}
          endIcon={<SendIcon />}
          loading={processing}
          loadingPosition="end"
          variant="contained"
        >
          <span>Convert</span>
        </LoadingButton>
        <Box  sx={{width: '80%'}}>
          <TabContext value={activeTab}>
            <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
              <TabList onChange={handleChangeTab} aria-label="XML and RDF selector">
                <Tab label="XML" value="xml" />
                <Tab label="RDF" value="rdf" />
                <Tab label="Graph" value="graph" />
              </TabList>
            </Box>
            <TabPanel value="xml" >
              <DownloadableXMLBox xmlText={xmlText} />
            </TabPanel>
            <TabPanel value="rdf" >
              <DownloadableTTLBox ttlText={ttlText} />
            </TabPanel>
            <TabPanel value="graph" >
              <RDFGraph ttlText={ttlText} />
            </TabPanel>
          </TabContext>
        </Box>
      </Stack>
    </Container>
  );
}

export default MainWindow;
