import {Button, Col, Row, Table} from "react-bootstrap";
import {useState} from "react";
import axios from "axios";
import AlertDismissible from "../../alert/alert";

interface ReportCardParams {
  reportItem: ReportItem;
}

export interface ReportItem {
  filing_date: string;
  form_description: string;
  form_link: string;
  form_type: string;
  reporting_date: string;
}

interface ReportBuybackStats {
  authorized: Array<Stats>;
  repurchased: Array<Stats>;
}

interface Stats {
  amount?: string;
  date: string;
  number?: string;
}

const ReportCard = (params: ReportCardParams) => {
  const [retryScan, setRetryScan] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [hideStats, setHideStats] = useState(false);
  const [reportInfo, setReportInfo] = useState<ReportBuybackStats>({authorized: Array<Stats>(), repurchased: Array<Stats>()});

  const getReportInfo = async () => {
    try {
      setIsLoading(true);
      const result = await axios.get<ReportBuybackStats>(`http://127.0.0.1:5000/report/buyback/stats?report_url=${params.reportItem.form_link}`, {
        headers: {
          Accept: "application/json"
        }
      })

      if (result.data.repurchased.length == 0 && result.data.authorized.length == 0) {
        setRetryScan(true);
        setReportInfo({repurchased: Array<Stats>(), authorized: Array<Stats>()})
      } else {
        setReportInfo(result.data);
        setRetryScan(false);
      }

      setIsLoading(false);
    } catch (error) {
      console.log(error);
      setReportInfo({repurchased: Array<Stats>(), authorized: Array<Stats>()})
      setIsLoading(false);
    }
  }

  const statsTable = (name: string, stats: Array<Stats>) => {
    return (
      <div>
        <h5>{name}</h5>
        <Table striped bordered hover size="sm">
          <thead>
          <tr>
            <th>#</th>
            <th>Date</th>
            <th>Amount</th>
            <th>Number</th>
          </tr>
          </thead>
          <tbody>
          {stats.length > 0 && stats.map((s: Stats, index) => {
            return (
              <tr>
                <td>{index}</td>
                <td>{s.date}</td>
                <td>{s.amount}</td>
                <td>{s.number}</td>
              </tr>)
          })}
          </tbody>
        </Table>
      </div>
    )

  }

  const anyAuthorizedInfo = (): boolean => {
    return reportInfo.authorized.length > 0;
  }

  const anyRepurchasedInfo = (): boolean => {
    return reportInfo.repurchased.length > 0;
  }

  const showCloseBtn = (): boolean => {
    return anyAuthorizedInfo() || anyRepurchasedInfo();
  }

  const toggleStats = () => {
    setHideStats(!hideStats)
  }

  return (
    <div className="border border-top-1 shadow-sm p-3 m-2">
      <Row>
        <Col>
          <p><a href={params.reportItem.form_link} target="_blank">{params.reportItem.form_description}</a></p>
        </Col>
        <Col>
          <p><strong>Form Type:</strong> {params.reportItem.form_type}</p>
          <p><strong>Filing Date:</strong> {params.reportItem.filing_date}</p>
          <p><strong>Reporting Date:</strong> {params.reportItem.reporting_date}</p>
        </Col>
        <Col className="d-flex justify-content-center align-items-center">
          <div>
            {(!showCloseBtn() && !retryScan) && <Button variant="outline-dark" disabled={isLoading} onClick={async () => await getReportInfo()}>{isLoading ? "Scanning financial report..." : "Learn More"}</Button>}
            {retryScan && <Button variant="outline-dark" disabled={isLoading} onClick={async () => await getReportInfo()}>{isLoading ? "Scanning financial report..." : "Retry Scan"}</Button>}
            {showCloseBtn() && <Button variant="outline-dark" onClick={toggleStats}>{hideStats ? "Open" : "Close"}</Button>}
          </div>
        </Col>
      </Row>
      {retryScan && <AlertDismissible variant="info" text1="No data found" text2="Neither authorized nor repurchased data were found inside this report." />}
      {(anyAuthorizedInfo() && !hideStats && !retryScan) && statsTable("Authorized Stock Repurchase Program", reportInfo.authorized)}
      {(anyRepurchasedInfo() && !hideStats && !retryScan) && statsTable("Stock Repurchases", reportInfo.repurchased)}
    </div>
  )
}

export default ReportCard;
