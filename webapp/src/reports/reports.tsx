import React, {useState} from "react";
import Search from "../search/search";
import ReportCard, {ReportItem} from "./reportCard/reportCard";
import axios from "axios";
import AlertDismissible from "../alert/alert";
import {Col, FormControl, FormGroup, Row, Spinner} from "react-bootstrap";

interface ReportListDto {
  reports: Array<ReportItem>;
}

const Reports = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [reportItems, setReportItems] = useState(Array<ReportItem>());
  const [filteredReportItems, setFilteredReportItems] = useState(Array<ReportItem>());
  const [isErrored, setIsErrored] = useState(false);
  const [searchedTerm, setSearchedTerm] = useState("");

  const getReportList = async (searchTerm: string) => {
    setIsLoading(true);
    setReportItems(Array<ReportItem>());
    setSearchedTerm(searchTerm);
    setIsErrored(false);
    try {
      const result = await axios.get<ReportListDto>(`http://127.0.0.1:5000/report/list/${searchTerm}`, {
        headers: { Accept: "application/json" }
      })
      setReportItems(result.data.reports);
      setFilteredReportItems(result.data.reports);
      setIsLoading(false);
    } catch (error) {
      console.log(error);
      setIsErrored(true);
      setIsLoading(false);
      return Array<ReportItem>();
    }
  }

  const filterReports = (e: React.ChangeEvent<HTMLInputElement|HTMLTextAreaElement>) => {
    if (!e.target.value) {
      setFilteredReportItems(reportItems);
      return
    }

    const filter = e.target.value.toLowerCase()
    let filteredReports = [];

    filteredReports = reportItems.filter((item: ReportItem) => {
      if (item.reporting_date.toLowerCase().includes(filter) ||
        item.filing_date.toLowerCase().includes(filter) ||
        item.form_description.toLowerCase().includes(filter) ||
        item.form_type.toLowerCase().includes(filter)) {

        return item;
      }
    });

    setFilteredReportItems(filteredReports);
  }

  return (
    <>
      <Row>
        <Col>
          {isErrored && <AlertDismissible variant="danger" text1="Error making request" text2="Please try again!"/>}
          {(searchedTerm && !isLoading && !isErrored && reportItems.length == 0) && <AlertDismissible variant="warning" text1="No report items found" text2="If you think this is wrong, please try again" />}
          <Search searchRequestCallbackFn={getReportList} />
          {(searchedTerm && reportItems.length > 0) && <h5>Results for: {searchedTerm}</h5>}
        </Col>
      </Row>
      {reportItems.length > 0 && (
        <Row>
          <Col md={8} />
          <Col md={4}>
            <FormGroup>
              <FormControl type="text" onChange={filterReports} placeholder="Filter results here..." />
            </FormGroup>
          </Col>
        </Row>
      )}
      <Row>
        <Col>
          {isLoading && (
            <div className="d-flex justify-content-center mt-3 pt-5">
              <Spinner animation="border" />
            </div>
          )}
          {reportItems.length > 0 && filteredReportItems.map((item: ReportItem) => <ReportCard reportItem={item} /> )}
        </Col>
      </Row>
    </>
  )
}

export default Reports;
