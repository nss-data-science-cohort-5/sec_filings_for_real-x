import React from 'react';
import './App.css';
import Search from "./search/search";
import {Col, Container, Row} from "react-bootstrap";
import Reports from "./reports/reports";

function App() {
  return (
    <Container>
      <Row>
        <Col>
          <Reports />
        </Col>
      </Row>
    </Container>
  );
}

export default App;
