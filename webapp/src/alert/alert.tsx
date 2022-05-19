import {useState} from "react";
import {Alert} from "react-bootstrap";

interface AlertParams {
  variant: string;
  text1: string;
  text2: string;
}

const AlertDismissible = (params: AlertParams) => {
  const [show, setShow] = useState(true);

  if (show) {
    return (
      <Alert variant={params.variant} className="mt-4" onClose={() => setShow(false)} dismissible>
        <p><strong>{params.text1}</strong> {params.text2}</p>
      </Alert>
    );
  } else {
    return null;
  }
}

export default AlertDismissible
