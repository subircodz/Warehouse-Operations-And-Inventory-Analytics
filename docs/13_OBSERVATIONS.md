# Observations

> **Case Study:** Warehouse Operations & Inventory Analytics  
> **Status:** 🟢 In Progress  
> **Methodology:** Data Analytics Project Methodology (DAPM Framework)

---

## Phase 1 – Business Understanding

<table>
  <thead>
    <tr>
      <th width="120">ID</th>
      <th>Observation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>OBS-001</td>
      <td>The warehouse stores multiple categories of consumer goods, including foods, beverages, personal care products, and household products.</td>
    </tr>
    <tr>
      <td>OBS-002</td>
      <td>The warehouse serves as a central facility for receiving, storing, and dispatching inventory.</td>
    </tr>
    <tr>
      <td>OBS-003</td>
      <td>Inventory movement follows a standard workflow: Goods Received → Storage → Order Picking → Dispatch.</td>
    </tr>
    <tr>
      <td>OBS-004</td>
      <td>The client is experiencing stock-related challenges, including stockouts, overstock, and inventory mismatches.</td>
    </tr>
    <tr>
      <td>OBS-005</td>
      <td>Delayed deliveries and customer complaints indicate operational inefficiencies that require investigation.</td>
    </tr>
    <tr>
      <td>OBS-006</td>
      <td>Inventory accuracy and inventory visibility are important concerns for warehouse operations.</td>
    </tr>
    <tr>
      <td>OBS-007</td>
      <td>Management requires data-driven insights to improve inventory control and operational efficiency.</td>
    </tr>
    <tr>
      <td>OBS-008</td>
      <td>The root causes of the identified business problems are currently unknown and will be investigated in later DAPM phases.</td>
    </tr>
  </tbody>
</table>

---

## Phase 2 – Stakeholder Analysis

<table>
  <thead>
    <tr>
      <th width="120">ID</th>
      <th>Observation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>OBS-009</td>
      <td>The Inventory Manager is responsible for monitoring inventory levels and maintaining stock availability.</td>
    </tr>
    <tr>
      <td>OBS-010</td>
      <td>The Procurement Team manages purchase orders and replenishment decisions based on inventory demand.</td>
    </tr>
    <tr>
      <td>OBS-011</td>
      <td>The Warehouse Manager oversees warehouse operations, including receiving, storage, order fulfillment, and dispatch.</td>
    </tr>
    <tr>
      <td>OBS-012</td>
      <td>The Logistics Team is responsible for shipment planning, dispatch, and delivery performance.</td>
    </tr>
    <tr>
      <td>OBS-013</td>
      <td>The Finance Department monitors inventory valuation and inventory-related operational costs.</td>
    </tr>
    <tr>
      <td>OBS-014</td>
      <td>Different stakeholders are responsible for different business functions and therefore require different analytical views of the same operational data.</td>
    </tr>
  </tbody>
</table>

---

## Phase 3 – Business Requirements

<table>
  <thead>
    <tr>
      <th width="120">ID</th>
      <th>Observation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>OBS-015</td>
      <td>Different stakeholders require different business information to support their daily operational decisions.</td>
    </tr>
    <tr>
      <td>OBS-016</td>
      <td>The Inventory Manager requires stock visibility, inventory movement, and stock status metrics.</td>
    </tr>
    <tr>
      <td>OBS-017</td>
      <td>The Procurement Team requires inventory levels, reorder status, supplier lead time, and demand trends.</td>
    </tr>
    <tr>
      <td>OBS-018</td>
      <td>The Warehouse Manager requires warehouse utilization, inventory accuracy, goods movement, and order processing metrics.</td>
    </tr>
    <tr>
      <td>OBS-019</td>
      <td>The Logistics Team requires dispatch readiness, delivery status, delayed deliveries, and vehicle utilization metrics.</td>
    </tr>
    <tr>
      <td>OBS-020</td>
      <td>The Finance Department requires inventory valuation, procurement costs, storage costs, holding costs, and dead stock analysis.</td>
    </tr>
    <tr>
      <td>OBS-021</td>
      <td>Sales and Customer Support require product availability, delayed orders, customer complaints, returns, and incorrect shipment information.</td>
    </tr>
    <tr>
      <td>OBS-022</td>
      <td>Although stakeholders require different reports, they all rely on the same warehouse operational data.</td>
    </tr>
  </tbody>
</table>


---

## Phase 4 – Data Discovery

<table>
<thead>
<tr>
<th width="120">ID</th>
<th>Observation</th>
</tr>
</thead>

<tbody>

<tr>
<td>OBS-23</td>
<td>The primary operational data is maintained within the Warehouse Management System (WMS).</td>
</tr>

<tr>
<td>OBS-023</td>
<td>Additional business reports are available as Microsoft Excel workbooks.</td>
</tr>

<tr>
<td>OBS-024</td>
<td>CSV exports are available for data analysis without direct database access.</td>
</tr>

<tr>
<td>OBS-025</td>
<td>The required datasets have been successfully identified and acquired for analysis.</td>
</tr>

<tr>
<td>OBS-026</td>
<td>Client-provided datasets have been organized under the <code>data/raw/</code> directory to preserve the original source data.</td>
</tr>

<tr>
<td>OBS-027</td>
<td>The project is ready to proceed to Data Validation.</td>
</tr>

</tbody>
</table>

---

### Navigating Documents

| Document | Link |
|----------|------|
| PROJECT_BRIEF | [01_PROJECT_BRIEF.md](01_PROJECT_BRIEF.md) |
| BUSINESS_UNDERSTANDING | [02_BUSINESS_UNDERSTANDING.md](02_BUSINESS_UNDERSTANDING.md) |
| STAKEHOLDER_ANALYSIS | [03_STAKEHOLDER_ANALYSIS.md](03_STAKEHOLDER_ANALYSIS.md) |
| BUSINESS_REQUIREMENTS | [04_BUSINESS_REQUIREMENTS.md](04_BUSINESS_REQUIREMENTS.md) |
| DATA_DISCOVERY | [05_DATA_DISCOVERY.md](05_DATA_DISCOVERY.md) |
| DATA_VALIDATION | [06_DATA_VALIDATION.md](06_DATA_VALIDATION.md) |
| DATA_PREPARATION | [07_DATA_PREPARATION.md](07_DATA_PREPARATION.md) |
| EDA_REPORT | [08_EDA_REPORT.md](08_EDA_REPORT.md) |
| BUSINESS_INSIGHTS | [09_BUSINESS_INSIGHTS.md](09_BUSINESS_INSIGHTS.md) |
| RECOMMENDATIONS | [10_RECOMMENDATIONS.md](10_RECOMMENDATIONS.md) |
| EXECUTIVE_SUMMARY | [11_EXECUTIVE_SUMMARY.md](11_EXECUTIVE_SUMMARY.md) |
| PROJECT_SUMMARY | [12_PROJECT_SUMMARY.md](12_PROJECT_SUMMARY.md) |
| OBSERVATIONS | [13_OBSERVATIONS.md](13_OBSERVATIONS.md) |
| ANALYTICAL_THINKING | [14_ANALYTICAL_THINKING.md](14_ANALYTICAL_THINKING.md) |
| PHASE_CHECKLIST | [15_PHASE_CHECKLIST.md](15_PHASE_CHECKLIST.md) |
| PROJECT README | [PROJECT README](../README.md) |
