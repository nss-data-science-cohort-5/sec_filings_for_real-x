import {useState} from "react";
import Search from "../search/search";
import ReportCard, {ReportItem} from "./reportCard/reportCard";
import axios from "axios";
import AlertDismissible from "../alert/alert";
import {Col, Row, Spinner} from "react-bootstrap";

interface ReportListDto {
  reports: Array<ReportItem>;
}

const Reports = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [reportItems, setReportItems] = useState(Array<ReportItem>());
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
      setIsLoading(false);
    } catch (error) {
      console.log(error);
      setIsErrored(true);
      setIsLoading(false);
      return Array<ReportItem>();
    }
  }

  return (
    <Row>
      <Col>
        {isErrored && <AlertDismissible variant="danger" text1="Error making request" text2="Please try again!"/>}
        {(searchedTerm && !isLoading && !isErrored && reportItems.length == 0) && <AlertDismissible variant="warning" text1="No report items found" text2="If you think this is wrong, please try again" />}
        <Search searchRequestCallbackFn={getReportList} />
        {(searchedTerm && reportItems.length > 0) && <h5>Results for: {searchedTerm}</h5>}
        {isLoading && (
          <div className="d-flex justify-content-center mt-3 pt-5">
            <Spinner animation="border" />
          </div>
        )}
        {reportItems.length > 0 && reportItems.map((item: ReportItem) => <ReportCard reportItem={item} /> )}
      </Col>
    </Row>
  )
}

export default Reports;
