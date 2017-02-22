import { Angular2HelloWorldPage } from './app.po';

describe('angular2-hello-world App', () => {
  let page: Angular2HelloWorldPage;

  beforeEach(() => {
    page = new Angular2HelloWorldPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
