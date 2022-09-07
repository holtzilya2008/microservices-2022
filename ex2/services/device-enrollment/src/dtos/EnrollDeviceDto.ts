export class EnrollDeviceDto {
  name: string;
  description: string;
  version: string;
  properties?: { [propName: string]: string };
}
