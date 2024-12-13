import {React, useState} from "react";
import SyntaxHighlighter from 'react-syntax-highlighter';
import { atomOneLight } from 'react-syntax-highlighter/dist/esm/styles/hljs';
import IconButton from '@mui/material/IconButton';
import DownloadIcon from '@mui/icons-material/Download';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import DownloadableTTLBoxStyles from './DownloadableTTLBox.module.css';
import Snackbar from '@mui/material/Snackbar';
import { saveAs } from 'file-saver';


function DownloadableTTLBox({ttlText}) {
  const [viewCopiedToClipboard, setViewCopiedToClipboard] = useState(false);

  const handleCloseCopiedToClipboard = () => {
    setViewCopiedToClipboard(false);
  };

  const copyToClipboard = async (text) => {
    try {
      console.log(text);
      //let beautyText = beautify(text);
      //console.log(beautyText);
      await navigator.clipboard.writeText(text);
      setViewCopiedToClipboard(true);
    } catch (error) {
      console.log(error);
      alert('Error copying to clipboard:', error);
    }
  };

  const download = (text) => {
    //let beautyText = beautify(text);
    var blob = new Blob([text], {type: "application/xml;charset=utf-8"});
    saveAs(blob, "report.ttl");
  }

  return (
    <Box className={DownloadableTTLBoxStyles.BoxStyle}>
      <Stack direction="row" justifyContent="flex-end">
        <IconButton aria-label="copy" onClick={() => {copyToClipboard(ttlText)}}>
          <ContentCopyIcon />
        </IconButton>
        <IconButton aria-label="download" onClick={() => {download(ttlText)}}>
          <DownloadIcon />
        </IconButton>
      </Stack>
      <Box className={DownloadableTTLBoxStyles.TTLViewerStyle}>
        <SyntaxHighlighter language="turtle" style={atomOneLight} wrapLongLines={true} children={ttlText} customStyle={{backgroundColor: "white"}} codeTagProps={{style: {fontFamily: 'monospace'} }}/>
      </Box>
      <Snackbar
          open={viewCopiedToClipboard}
          onClose={handleCloseCopiedToClipboard}
          message="Copied to clipboard!"
          autoHideDuration={2000}/>
    </Box>
  );
}

export default DownloadableTTLBox;
