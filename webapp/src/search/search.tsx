import {Button, Col, Form, Row} from "react-bootstrap";
import React, {useState} from "react";

interface SearchParams {
  searchRequestCallbackFn: (searchTerm: string) => void;
}

const Search = (params: SearchParams) => {
  const [isLoading, setLoading] = useState(false);
  const [searchTerm, setSearchTerm] = useState("");

  const search = async () => {
    setLoading(true);
    await params.searchRequestCallbackFn(searchTerm);
    setLoading(false);
  }

  const handleChange = (e: React.ChangeEvent<HTMLInputElement|HTMLTextAreaElement>) => {
    setSearchTerm(e.target.value)
  }

  return (
    <Row className="pt-5">
      <Col md={3}>
        <h4>Company Search</h4>
      </Col>
      <Col md={6}>
        <Form>
          <Form.Group>
            <Form.Control type="input" placeholder="Enter company name, ticker symbol, or CIK" onChange={(e) => handleChange(e)} />
            <Form.Text>Eg: nflx, appl, goog, apog, bbw</Form.Text>
          </Form.Group>
        </Form>
      </Col>
      <Col md={3}>
        <Button
          variant="outline-primary"
          type="submit"
          disabled={isLoading}
          onClick={async () => await search()}>
          {isLoading ? "Discovering company reports..." : "Click to Search"}
        </Button>
      </Col>
    </Row>
  )
}

export default Search;
