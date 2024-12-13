import {React, useState} from "react";
import XMLViewer from "react-xml-viewer";
import IconButton from '@mui/material/IconButton';
import DownloadIcon from '@mui/icons-material/Download';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';
import Box from '@mui/material/Box';
import Stack from '@mui/material/Stack';
import DownloadableXMLBoxStyles from './DownloadableXMLBox.module.css';
import beautify from "xml-beautifier";
import Snackbar from '@mui/material/Snackbar';
import { saveAs } from 'file-saver';


function DownloadableXMLBox({xmlText}) {
  const [viewCopiedToClipboard, setViewCopiedToClipboard] = useState(false);

  const handleCloseCopiedToClipboard = () => {
    setViewCopiedToClipboard(false);
  };

  const copyToClipboard = async (text) => {
    try {
      let beautyText = beautify(text);
      await navigator.clipboard.writeText(beautyText);
      setViewCopiedToClipboard(true);
    } catch (error) {
      console.log(error);
      alert('Error copying to clipboard:', error);
    }
  };

  const download = (text) => {
    let beautyText = beautify(text);
    var blob = new Blob([beautyText], {type: "application/xml;charset=utf-8"});
    saveAs(blob, "report.xml");
  }

  return (
    <Box className={DownloadableXMLBoxStyles.BoxStyle}>
      <Stack direction="row" justifyContent="flex-end">
        <IconButton aria-label="copy" onClick={() => {copyToClipboard(xmlText)}}>
          <ContentCopyIcon />
        </IconButton>
        <IconButton aria-label="download" onClick={() => {download(xmlText)}}>
          <DownloadIcon />
        </IconButton>
      </Stack>
      <Box className={DownloadableXMLBoxStyles.XMLViewerStyle}>
        <XMLViewer xml={xmlText} collapsible />
      </Box>
      <Snackbar
          open={viewCopiedToClipboard}
          onClose={handleCloseCopiedToClipboard}
          message="Copied to clipboard!"
          autoHideDuration={2000}/>
    </Box>
  );
}

export default DownloadableXMLBox;
